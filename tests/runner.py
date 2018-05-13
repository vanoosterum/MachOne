import unittest

# import your test modules
import login_page
import feedback_page

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(login_page))
suite.addTests(loader.loadTestsFromModule(feedback_page))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
