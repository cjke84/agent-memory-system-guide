from pathlib import Path


def test_readme_mentions_openviking_optional():
    repo_root = Path('/Users/jingkechen/Documents/agent-memory-system-guide')
    readme_text = (repo_root / 'README.md').read_text(encoding='utf-8')
    assert 'OpenViking is an optional enhancement' in readme_text
    assert 'not required for the core workflow' in readme_text
