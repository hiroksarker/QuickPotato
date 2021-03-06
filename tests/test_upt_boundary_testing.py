from QuickPotato.profiling.intrusive import unit_performance_test as upt
from QuickPotato.database.queries import Crud
from QuickPotato.configuration.management import options
from demo.example_code import *
import unittest

SAMPLE_SIZE = 10
UNIT_TEST_DATABASE_NAME = "upt_unit_tests_regression_detection_with_t_test"


class TestBoundariesEndToEnd(unittest.TestCase):

    def setUp(self):
        """

        """
        options.enable_intrusive_profiling = True

    def tearDown(self):
        """

        """
        options.enable_intrusive_profiling = False

    @staticmethod
    def clean_up_database():
        """

        """
        database_manager = Crud()
        database_manager.delete_result_database(UNIT_TEST_DATABASE_NAME)

    def test_output_with_no_breached_boundary(self):
        """

        """
        # Define Test Case
        upt.test_case_name = UNIT_TEST_DATABASE_NAME
        upt.max_and_min_boundary_for_average = {"max": 1, "min": 0.001}

        # Execute method under test
        for _ in range(0, SAMPLE_SIZE):
            slow_method()

        # Analyse profiled results
        results = upt.verify_benchmark_against_set_boundaries

        self.assertTrue(results)

    def test_output_with_breached_boundary(self):
        """

        """
        # Define Test Case
        upt.test_case_name = UNIT_TEST_DATABASE_NAME
        upt.max_and_min_boundary_for_average = {"max": 0.010, "min": 0.001}

        # Execute method under test
        for _ in range(0, SAMPLE_SIZE):
            slow_method()

        # Analyse profiled results
        results = upt.verify_benchmark_against_set_boundaries

        self.assertFalse(results)

    def test_output_with_all_boundaries_enabled(self):
        """

        """
        # Define Test Case
        upt.test_case_name = UNIT_TEST_DATABASE_NAME
        upt.max_and_min_boundary_for_average = {"max": 1, "min": 0.001}
        upt.max_and_min_boundary_for_largest_outlier = {"max": 1, "min": 0.001}
        upt.max_and_min_boundary_for_percentile_5th = {"max": 1, "min": 0.001}
        upt.max_and_min_boundary_for_percentile_10th = {"max": 1, "min": 0.001}
        upt.max_and_min_boundary_for_percentile_15th = {"max": 1, "min": 0.001}
        upt.max_and_min_boundary_for_percentile_20th = {"max": 1, "min": 0.001}
        upt.max_and_min_boundary_for_percentile_25th = {"max": 1, "min": 0.001}
        upt.max_and_min_boundary_for_percentile_30th = {"max": 1, "min": 0.001}
        upt.max_and_min_boundary_for_percentile_35th = {"max": 1, "min": 0.001}
        upt.max_and_min_boundary_for_percentile_40th = {"max": 1, "min": 0.001}
        upt.max_and_min_boundary_for_percentile_45th = {"max": 1, "min": 0.001}
        upt.max_and_min_boundary_for_percentile_50th = {"max": 1, "min": 0.001}
        upt.max_and_min_boundary_for_percentile_55th = {"max": 1, "min": 0.001}
        upt.max_and_min_boundary_for_percentile_60th = {"max": 1, "min": 0.001}
        upt.max_and_min_boundary_for_percentile_65th = {"max": 1, "min": 0.001}
        upt.max_and_min_boundary_for_percentile_70th = {"max": 1, "min": 0.001}
        upt.max_and_min_boundary_for_percentile_75th = {"max": 1, "min": 0.001}
        upt.max_and_min_boundary_for_percentile_80th = {"max": 1, "min": 0.001}
        upt.max_and_min_boundary_for_percentile_85th = {"max": 1, "min": 0.001}
        upt.max_and_min_boundary_for_percentile_90th = {"max": 1, "min": 0.001}
        upt.max_and_min_boundary_for_percentile_95th = {"max": 1, "min": 0.001}

        # Execute method under test
        for _ in range(0, SAMPLE_SIZE):
            slow_method()

        # Analyse profiled results
        results = upt.verify_benchmark_against_set_boundaries

        self.assertTrue(results)
