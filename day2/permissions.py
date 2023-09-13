from enum import Enum, auto
import urllib.request
import sys
import inspect

class Permissions(Enum):
    """Permissions constants"""
    NETWORK = auto()
    FILESYSTEM = auto()


def has_permission(permission: Permissions):
    match permission:
        case Permissions.NETWORK:
            return "--network" in sys.argv
        case Permissions.FILESYSTEM:
            return False


def requires_permission(permission: Permissions):
    def decorator(f):
        def inner(*args, **kwargs):
            if not has_permission(permission):
                raise Exception("Not Authorized")
            return f(*args, **kwargs)
        inner.permissions = f.__dict__.get('permissions', []) + [permission]
        return inner
    return decorator


@requires_permission(Permissions.NETWORK)
def find_my_ip():
    with urllib.request.urlopen('https://api.ipify.org') as response:
        data = response.read()
        return data.decode('utf8')


@requires_permission(Permissions.FILESYSTEM)
def list_users():
    with open('/etc/passwd') as f:
        print(f.read())




def init():
    safe_functions = {'has_permission', 'init', 'requires_permission'}
    functions = [(name, obj) for name, obj in inspect.getmembers(sys.modules[__name__])
                 if inspect.isfunction(obj)
                 and 'permissions' not in obj.__dict__
                 and name not in safe_functions]
    if len(functions) > 0:
        raise Exception(f"Functions {functions} don't define required permissions")


init()
print(find_my_ip())
# list_users()
