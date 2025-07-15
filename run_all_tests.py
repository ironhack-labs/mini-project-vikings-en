#!/usr/bin/env python3
#Simple test runner that correctly detects test results

import subprocess  #new* skip the CMD#
import sys         #new* access to Python interpreter and system functions
import os          #new* operating system interface

def main():
    print("VIKINGS GAME - TEST RUNNER \n")
    
    # Test files to run
    test_files = [
        ("1-testsSoldier.py", "Soldier"),
        ("2-testsVikings.py", "Viking"),
        ("3-testsSaxons.py", "Saxon"),
        ("4-testsWar.py", "War")
    ]
    
    all_passed = True
    results = []
    
    #Test Execution Loop
    for filename, class_name in test_files:
    
        print(f"Testing {class_name} Class...")
    
        try:
            # Run the test
            result = subprocess.run(
                [sys.executable, filename], 
                capture_output=True, 
                text=True
            )
            
            # Check if passed by looking at return code
            passed = (result.returncode == 0)
            
            if passed:
                print(f"{class_name} tests: PASSED")
                
                # Count how many tests ran
                output_lines = result.stderr.split('\n')
                for line in output_lines:
                    if "Ran" in line and "test" in line:
                        print(f"   {line.strip()}")
            else:
                print(f"{class_name} tests: FAILED")
                all_passed = False
                # Show the errors
                if result.stderr:
                    print("\nErrors:")
                    print(result.stderr)
            
            results.append((class_name, passed))
            
        except FileNotFoundError:
            print(f"Could not find {filename}")
            results.append((class_name, False))
            all_passed = False
    
    # Final summary
    print("\nSUMMARY")

    
    for class_name, passed in results:
        status = "PASSED" if passed else " FAILED"
        print(f"{class_name}: {status}")
    

    if all_passed:
        print(" ALL TESTS PASSED! Your game is ready!")
    else:
        print(" Some tests failed. Check the details above.")

if __name__ == "__main__":
    main()