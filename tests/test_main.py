import os
from nixpy import main as m


def test_main():
    assert m.nix_check()

def test_to_wsl():
    if os.name == "nt":
        assert m.to_wsl("C:\\Users\\User") == "/mnt/c/Users/User"
        assert m.to_wsl("\\\\Server\\Share") == "./\\\\Server/Share"
    else:
        assert m.to_wsl("/home/user") == "/home/user"

def test_nix_run():
    proc = m.nix_run(["echo Hello, Nix!"])
    assert proc.returncode == 0
    assert "Hello, Nix!" in proc.stdout