import yaml
from rez.resolved_context import ResolvedContext

ctx = ResolvedContext(['maya', 'usd'])
# get rez packages list as below:
# ['maya-2017.3', 'python-2.7.5', ...]
packages = ['{0}-{1}'.format(package.name, package.version) for package in
            ctx.resolved_packages]
print(packages)

# save(cache) rez resolved packages to a yaml file.
context = {'packages': packages}
filePath = '/tmp/maya.rtx'
with open(filePath, 'w') as f:
    yaml.dump(context, f)

# run maya with rez environment
with open(filePath, 'r') as f:
    context = yaml.load(f)
    ctx = ResolvedContext(context.get('packages'))
    # run maya in the rez environment
    retcode, out, err = ctx.execute_shell(command=["which", "maya"],
                                          block=True)
    print(out)
