from openapi_parser.exporter import PackageWriter
from openapi_parser.parser.loader import OpenApiParser

def main():
    parser = OpenApiParser.open('swagger/swagger_external.yaml')
    parser.load_all()

    package_writer = PackageWriter(parser)
    package_writer.write_package()

    return 0

if (__name__ == '__main__'):
    exit_code = main()
    exit(exit_code)