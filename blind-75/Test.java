public class Test {
    
    /**
    * This will do a standard comparison between two inputs and
    * return either true or false. The inputs can by any variable
    * type.
    * @param <T>       This allows for any type of output
    * @param actual    First input to test
    * @param expected  Second input to test
    * @param testName  Name of test for output
    */
  
  public <T> boolean assertEqual(String testName, T actual, T expected){
    boolean success = assertEqual(actual, expected);
    System.out.println("Test: " + testName);
    if (success) {
      System.out.println("Test Passes");
    }
    else {
      System.out.println("Test Fails");
    }
    System.out.println();
    return success;
  }
  
  public <T> boolean assertEqual(T actual, T expected){
    System.out.println("Actual is: " + actual);
    System.out.println("Expected got: " + expected);
    return actual.equals(expected);
  }

}