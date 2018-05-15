import unittest

# import your test modules
import try_out
# import feedback_page

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(try_out))
# suite.addTests(loader.loadTestsFromModule(feedback_page))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=5)
result = runner.run(suite)
