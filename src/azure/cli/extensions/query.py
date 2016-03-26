def register(application):
    def register_global_parameter(parser):
        # Let the program know that we are adding a parameter --query
        parser.add_argument('--query', dest='_jmespath_query', metavar='JMESPATH',
                            help='JMESPath query string. See http://jmespath.org/ for more information and examples.') # pylint: disable=line-too-long

    def handle_query_parameter(args):
        # Of there is a query specified on the command line, we'll take care of that!
        try:
            query_value = args._jmespath_query #  pylint: disable=protected-access
            del args._jmespath_query

            if query_value:
                def filter_output(event_data):
                    import jmespath
                    event_data['result'] = jmespath.search(query_value, event_data['result'])

                application.register(application.FILTER_RESULT, filter_output)

        except AttributeError:
            pass

    application.register(application.GLOBAL_PARSER_CREATED, register_global_parameter)
    application.register(application.COMMAND_PARSER_PARSED, handle_query_parameter)
