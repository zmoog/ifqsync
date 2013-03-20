
from optparse import make_option


class BaseCommand(object):
	
	option_list = (
		make_option('-v', '--verbosity', action='store', dest='verbosity', default='1', type='choice', choices=['0', '1', '2', '3']),
		make_option('-k', '--access_token_key'),
		make_option('-s', '--access_token_secret'),
		make_option('-a', '--archive_path'),
	)

	def execute(self, args, options):

		print "args: %s" % (args)
		print "options: %s" % (options)

		self.handle(args, options)


def handle_default_options(options):
	"""
	Include any default options that all commands should accept here
	so that ManagementUtility can handle them before searching for
	user commands.

	"""
	if options.settings:
		os.environ['DJANGO_SETTINGS_MODULE'] = options.settings
	if options.pythonpath:
		sys.path.insert(0, options.pythonpath)
	