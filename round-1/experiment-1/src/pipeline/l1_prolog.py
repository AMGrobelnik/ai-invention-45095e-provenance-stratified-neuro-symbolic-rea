"""L1: SWI-Prolog interface with depth-limited SLD resolution."""
import subprocess
import tempfile
import os
import re
from pathlib import Path
from loguru import logger


class PrologKB:
    """Manages a Prolog KB stored in a temp file, queried via subprocess."""

    def __init__(self):
        self._facts: list[str] = []  # raw Prolog strings
        self._fact_meta: list[dict] = []  # metadata per fact
        self._rules: list[str] = []
        self._tmpfile: str | None = None

    def load_l0_facts(self, facts: list[dict]):
        for f in facts:
            pred = f["predicate"]
            args = f["args"]
            atom = pred + "(" + ", ".join(args) + ")" if args else pred
            self._facts.append(atom + ".")
            self._fact_meta.append({
                "predicate": pred, "args": args,
                "tier": f.get("tier", "l0"),
                "confidence": f.get("confidence", 1.0),
                "source_span": f.get("source_span", "")
            })

    def load_rules(self, rules: list[str]):
        for r in rules:
            r = r.strip()
            if not r.endswith("."):
                r += "."
            self._rules.append(r)

    def get_all_fact_meta(self) -> list[dict]:
        return list(self._fact_meta)

    def _write_kb(self) -> str:
        if self._tmpfile and os.path.exists(self._tmpfile):
            return self._tmpfile
        with tempfile.NamedTemporaryFile(mode='w', suffix='.pl', delete=False) as f:
            f.write(":- set_prolog_flag(encoding, utf8).\n")
            for fact in self._facts:
                f.write(fact + "\n")
            for rule in self._rules:
                f.write(rule + "\n")
            self._tmpfile = f.name
        return self._tmpfile

    def invalidate_cache(self):
        if self._tmpfile and os.path.exists(self._tmpfile):
            os.unlink(self._tmpfile)
        self._tmpfile = None

    def assertz(self, atom: str, tier: str = "l1", confidence: float = 1.0):
        if not atom.endswith("."):
            atom_pl = atom + "."
        else:
            atom_pl = atom
        self._facts.append(atom_pl)
        # parse predicate/args from atom string
        m = re.match(r'^([a-z][a-z0-9_]*)\((.*)\)$', atom.rstrip('.'))
        if m:
            pred = m.group(1)
            args = [a.strip() for a in m.group(2).split(",")]
        else:
            pred = atom.rstrip('.')
            args = []
        self._fact_meta.append({"predicate": pred, "args": args, "tier": tier, "confidence": confidence, "source_span": ""})
        self.invalidate_cache()

    def query_with_depth_limit(self, goal: str, depth: int = 5) -> tuple[bool, str]:
        """Run goal with depth limit. Returns (proved, tier_string)."""
        kb_file = self._write_kb()

        # Escape goal for shell
        query = f"call_with_depth_limit(({goal}), {depth}, Result), (Result = depth_limit_exceeded -> write(depth_limit_exceeded) ; write(proved)), halt."
        swipl_cmd = ["swipl", "-q", "-f", kb_file, "-g", query, "-t", "halt"]

        try:
            result = subprocess.run(
                swipl_cmd, capture_output=True, text=True, timeout=10
            )
            stdout = result.stdout.strip()
            logger.debug(f"Prolog query '{goal}': stdout={stdout!r} returncode={result.returncode}")
            if "proved" in stdout:
                return True, "l1"
            return False, "depth_limit_exceeded" if "depth_limit_exceeded" in stdout else "failed"
        except subprocess.TimeoutExpired:
            logger.warning(f"Prolog query timed out: {goal}")
            return False, "timeout"
        except Exception as e:
            logger.warning(f"Prolog query error: {e}")
            return False, "error"

    def query_exists(self, predicate: str, args: list[str]) -> bool:
        """Check if exact ground atom exists in KB."""
        atom = predicate + "(" + ", ".join(args) + ")" if args else predicate
        return atom + "." in self._facts or atom in self._facts

    def __del__(self):
        if self._tmpfile and os.path.exists(self._tmpfile):
            try:
                os.unlink(self._tmpfile)
            except Exception:
                pass
