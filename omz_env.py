# coding: utf-8

# See: https://forum.omz-software.com/topic/2135/telling-if-i-m-pythonista-or-editorial-or-sublime-text-or-whatever

def omz_env():
    try:
        import workflow
        return 'Editorial'
    except ImportError:
        try:
            import scene
            return 'Pythonista'
        except ImportError:
            return None

env = omz_env()
print('Yeah!!  ' + env if env else 'Sublime or other non-OMZ Software platform.')
