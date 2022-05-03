c.Application.log_datefmt = '%Y-%m-%d %H:%M:%S'
c.Application.log_format = '[%(name)s]%(highlevel)s %(message)s'
c.Application.log_level = 30

c.JupyterHub.authenticator_class = 'jupyterhub.auth.PAMAuthenticator'

c.LocalAuthenticator.create_system_users = True

c.JupyterHub.bind_url = 'http://127.0.0.1:5050/'

#  Default: 'jupyterhub_config.py'
c.JupyterHub.config_file = '/usr/local/share/jupyterhub/jupyterhub_config.py'

## File in which to store the cookie secret.
#  Default: 'jupyterhub_cookie_secret'
c.JupyterHub.cookie_secret_file = '/usr/local/share/jupyterhub/jupyterhub_cookie_secret'

c.ConfigurableHTTPProxy.pid_file = '/usr/local/share/jupyterhub/jupyterhub-proxy.pid'

c.SudoSpawner.sudospawner_path = '/usr/local/share/jupyterhub/env/bin/sudospawner'

c.Spawner.default_url = '/tree/home/'

c.Spawner.notebook_dir='/usr/local/share/jupyterhub/'

c.Spawner.cmd = '/usr/local/share/jupyterhub/env/bin/jupyterhub-singleuser'

## The location of jupyterhub data files (e.g. /usr/local/share/jupyterhub)

c.JupyterHub.data_files_path = '/usr/local/share/jupyterhub/env/share/jupyterhub'

## url for the database. e.g. `sqlite:///jupyterhub.sqlite`
#  Default: 'sqlite:///jupyterhub.sqlite'
c.JupyterHub.db_url = 'sqlite:////usr/local/share/jupyterhub/jupyterhub.sqlite'

## log all database transactions. This has A LOT of output
#  Default: False
c.JupyterHub.debug_db = False

#  Default: '127.0.0.1'
c.JupyterHub.hub_ip = '127.0.0.1'

#  Defaults to an empty set, in which case no user has admin access.
#  Default: set()
# c.Authenticator.admin_users = set()
c.Authenticator.admin_users = {'jupyterhub'}

## Set of usernames that are allowed to log in.
#  
#  Use this with supported authenticators to restrict which users can log in.
#  This is an additional list that further restricts users, beyond whatever
#  restrictions the authenticator has in place. Any user in this list is granted
#  the 'user' role on hub startup.
#  
#  If empty, does not perform any additional restriction.
c.Authenticator.allowed_users = {'jupyterhub'}

##

## Docker spawner
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_CONTAINER']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
# See https://github.com/jupyterhub/dockerspawner/blob/master/examples/oauth/jupyterhub_config.py
c.JupyterHub.hub_ip = os.environ['HUB_IP']

# user data persistence
# see https://github.com/jupyterhub/dockerspawner#data-persistence-and-dockerspawner
#notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR')
#c.DockerSpawner.notebook_dir = notebook_dir
#c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }

# Other stuff
c.Spawner.cpu_limit = 1
c.Spawner.mem_limit = '10G'
