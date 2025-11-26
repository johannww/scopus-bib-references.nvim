import pybliometrics
import sys
key = sys.argv[1]
pybliometrics.scopus.init(keys=[key])
