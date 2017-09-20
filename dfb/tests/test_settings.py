import os
from pathlib import Path

from django.test import TestCase

from dfb.settings import get_environment_variable, get_environment_file_path, BASE_DIR


class SettingsTestCase(TestCase):

    def test_get_environment_file_path_returns_correct_path(self):
        env_file = Path(get_environment_file_path())
        self.assertTrue(env_file.exists())

    def test_base_dir_points_at_the_correct_dir(self):
        manage_py_file = Path(os.path.join(BASE_DIR, 'manage.py'))
        build_sh_file = Path(os.path.join(BASE_DIR, 'build.sh'))
        gitignore_file = Path(os.path.join(BASE_DIR, '.gitignore'))
        self.assertTrue(manage_py_file.exists())
        self.assertTrue(build_sh_file.exists())
        self.assertTrue(gitignore_file.exists())

    def test_get_environment_variable_reads_file_correctly(self):
        environment = get_environment_variable(os.path.join(BASE_DIR, "dfb", "tests", "TEST_ENVIRONMENT.cfg"))
        self.assertEqual(environment, "test_environment")
