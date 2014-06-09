from copy import copy
from datetime import date, datetime
from optparse import make_option, Option, OptionValueError


def check_date(option, opt, value):
	try:
		return datetime.strptime(value, "%Y%m%d")
	except ValueError:
		# print('VALUE ERROR')
		raise OptionValueError(
			"option %s: invalid date value: %r" % (opt, value))

class DateOption(Option):
	TYPES = Option.TYPES + ('date',)
	TYPE_CHECKER = copy(Option.TYPE_CHECKER)
	TYPE_CHECKER["date"] = check_date


class BaseCommand(object):

	option_list = (
		# make_option('-v', '--verbosity', action='store', dest='verbosity', default='1', type='choice', choices=['0', '1', '2', '3']),
		# make_option('-k', '--access_token_key'),
		# make_option('-s', '--access_token_secret'),
		# make_option('-a', '--archive_path'),
		DateOption("-t", "--target_date", action="store", type="date", dest="target_date", default=date.today()),
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
