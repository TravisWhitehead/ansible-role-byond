def test_dream_daemon(host):
    assert host.run('DreamDaemon -version').succeeded
