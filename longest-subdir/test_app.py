import os
from app import find_longest_subdirectory

def setup_test_environment(base_path):
    os.makedirs(os.path.join(base_path, 'bin'), exist_ok=True)
    os.makedirs(os.path.join(base_path, 'charts/beta/validations'), exist_ok=True)
    os.makedirs(os.path.join(base_path, 'ci'), exist_ok=True)
    os.makedirs(os.path.join(base_path, 'postgres/data/logs'), exist_ok=True)
    os.makedirs(os.path.join(base_path, 'script'), exist_ok=True)
    os.makedirs(os.path.join(base_path, 'templates'), exist_ok=True)

def teardown_test_environment(base_path):
    for root, dirs, files in os.walk(base_path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

def test_find_longest_subdirectory():
    test_dir = '/tmp/testdir'
    setup_test_environment(test_dir)
    
    longest_subdir = find_longest_subdirectory(test_dir)
    assert longest_subdir == 'validations'

    teardown_test_environment(test_dir)

def test_empty_directory():
    empty_dir = '/tmp/emptydir'
    os.makedirs(empty_dir, exist_ok=True)
    
    longest_subdir = find_longest_subdirectory(empty_dir)
    assert longest_subdir == ''
    
    os.rmdir(empty_dir)

def test_multiple_long_subdirectories():
    test_dir = '/tmp/testdir2'
    os.makedirs(os.path.join(test_dir, 'alpha/beta/gamma/delta'), exist_ok=True)
    os.makedirs(os.path.join(test_dir, 'epsilon/zeta/eta/theta'), exist_ok=True)
    
    longest_subdir = find_longest_subdirectory(test_dir)
    # Expecting 'delta' because it is deeper
    assert longest_subdir == 'delta'

    teardown_test_environment(test_dir)

if __name__ == "__main__":
    test_find_longest_subdirectory()
    test_empty_directory()
    test_multiple_long_subdirectories()
