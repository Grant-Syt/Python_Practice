from timeit import timeit

# pass globals() as local_globals in calls to this function
def timeTests(local_globals, function_prefix="test_", repeats=1):
    results = {}
    
    for name, func in dict(local_globals).items():
        if name.startswith(function_prefix):
            results[name] = timeit(func, number=repeats)
    
    if not results:
        print("\nNo matching tests to time, try adjusting the function_prefix "\
              "argument or your local function names.\n")
    else:
        print("")
        for name, time in sorted(results.items(), key=lambda x: x[1]):
            print('{:.5f} {}'.format(time, name))
        print("")