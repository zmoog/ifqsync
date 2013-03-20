import collections
import os
import sys
from optparse import OptionParser, NO_DEFAULT

from core.utils.importlib import import_module
from base import BaseCommand


class LaxOptionParser(OptionParser):
	"""
	An option parser that doesn't raise any errors on unknown options.

	This is needed because the --settings and --pythonpath options affect
	the commands (and thus the options) that are available to the user.
	"""
	def error(self, msg):
		pass

	def print_help(self):
		"""Output nothing.

		The lax options are included in the normal option parser, so under
		normal usage, we don't need to print the lax options.
		"""
		pass

	def print_lax_help(self):
		"""Output the basic options available to every command.

		This just redirects to the default print_help() behavior.
		"""
		OptionParser.print_help(self)

	def _process_args(self, largs, rargs, values):
		"""
		Overrides OptionParser._process_args to exclusively handle default
		options and ignore args and other options.

		This overrides the behavior of the super class, which stop parsing
		at the first unrecognized option.
		"""
		while rargs:
			arg = rargs[0]
			try:
				if arg[0:2] == "--" and len(arg) > 2:
					# process a single long option (possibly with value(s))
					# the superclass code pops the arg off rargs
					self._process_long_opt(rargs, values)
				elif arg[:1] == "-" and len(arg) > 1:
					# process a cluster of short options (possibly with
					# value(s) for the last one only)
					# the superclass code pops the arg off rargs
					self._process_short_opts(rargs, values)
				else:
					# it's either a non-default option or an arg
					# either way, add it to the args list so we can keep
					# dealing with options
					del rargs[0]
					raise Exception
			except:
				largs.append(arg)

def get_version():
	return (0, 1,)




class ManagementUtility(object):

	def __init__(self, argv=None):
		self.argv = argv or sys.argv[:]
		self.prog_name = os.path.basename(self.argv[0])

		#self.commands = dict(sync=SyncCommand())

	#def main_help_text(self, commands_only=False):
	#	"""
	#	Returns the script's main help text, as a string.
	#	"""
	#	if commands_only:
	#		usage = sorted(get_commands().keys())
	#	else:
	#		usage = [
	#			"",
	#			"Type '%s help <subcommand>' for help on a specific subcommand." % self.prog_name,
	#			"",
	#			"Available subcommands:",
	#		]
	#		commands_dict = collections.defaultdict(lambda: [])
	#		for name, app in six.iteritems(get_commands()):
	#			if app == 'django.core':
	#				app = 'django'
	#			else:
	#				app = app.rpartition('.')[-1]
	#			commands_dict[app].append(name)
	#		style = color_style()
	#		for app in sorted(commands_dict.keys()):
	#			usage.append("")
	#			usage.append(style.NOTICE("[%s]" % app))
	#			for name in sorted(commands_dict[app]):
	#				usage.append("    %s" % name)
	#	return '\n'.join(usage)

	def load_command_class(self, name):
		"""
		Given a command name and an application name, returns the Command
		class instance. All errors raised by the import process
		(ImportError, AttributeError) are allowed to propagate.
		"""
		module = import_module('core.management.commands.%s' % (name))
		return module.Command()


	def execute(self):
		"""
		Given the command-line arguments, this figures out which subcommand is
		being run, creates a parser appropriate to that command, and runs it.
		"""
		# Preprocess options to extract --settings and --pythonpath.
		# These options could affect the commands that are available, so they
		# must be processed early.
		parser = LaxOptionParser(usage="%prog subcommand [options] [args]",
			version=get_version(),
			option_list=BaseCommand.option_list)
		#self.autocomplete()
		try:
			options, args = parser.parse_args(self.argv)
			print options, args
			handle_default_options(options)
		except:
			pass # Ignore any option errors at this point.

		try:
			subcommand = self.argv[1]

			self.load_command_class(subcommand).execute(args, options)


		except IndexError:
			subcommand = 'help' # Display help if no arguments were given.


        
def execute_from_command_line(argv=None):
	"""
	A simple method that runs a ManagementUtility.
	"""
	utility = ManagementUtility(argv)
	utility.execute()


