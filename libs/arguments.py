import argparse
import re


def argparse_adapter(validator):
    parser = argparse.ArgumentParser(description='API для транскодирования файлов')

    for key, options in validator.items():
        large_key = '--{}'.format(key.replace('_', '-'))
        short_key = '-{}'.format(''.join(map(lambda x: x[0], key.split('_'))).lower())

        dest = key

        if 'regex' in options:
            def type_regex(s, pat=re.compile(options['regex'])):
                if not pat.match(s):
                    raise argparse.ArgumentTypeError
                return s

            arg_type = type_regex
        else:
            arg_type = options.get('type', str)

        default = options.get('default')
        help = options.get('help')
        required = options.get('required')

        parser.add_argument(large_key,
                            short_key,
                            dest=dest,
                            type=arg_type,
                            default=default,
                            help=help,
                            required=required
                            )

    return parser
