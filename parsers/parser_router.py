from logger.logger import get_logger

class ParserRouter():

    def __init__(self,parsers):
        self.parsers = parsers
        self.logger = get_logger(__name__)

    def parse(self,file_path):

        for parser in self.parsers:
            try:
                self.logger.info(f"{parser.__class__.__name__} started")
                parser_output = parser.parse(file_path)
                return parser_output
            except:
                self.logger.error(f"{parser.__class__.__name__} failed")
        raise RuntimeError("All Parsers Failed")