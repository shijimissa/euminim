def runtime_lavamoat_cache_editor(cache_file_path, delete_cache):
    """
    Function to delete the file at the given file path.

    Args:
        cache_file_path: The file path to the cache file.
        delete_cache: A boolean specifying whether to delete the cache file.

    Returns:
        None
    """
    if delete_cache:
        if os.path.exists(cache_file_path):
            os.remove(cache_file_path)
            print(f"Deleted file: {cache_file_path}")
        else:
            print(f"File does not exist: {cache_file_path}")
    else:
        print(f"File not deleted: {cache_file_path}")  
