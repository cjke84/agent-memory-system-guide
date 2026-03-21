from pathlib import Path


def test_install_mentions_openviking_optional():
    repo_root = Path('/Users/jingkechen/Documents/agent-memory-system-guide')
    install_text = (repo_root / 'INSTALL.md').read_text(encoding='utf-8')
    assert 'OpenViking as an optional enhancement' in install_text
    assert 'OpenViking 视为可选增强' in install_text
