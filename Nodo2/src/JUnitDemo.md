# JUnit Demo

[Official Page](https://junit.org/junit5/docs/current/user-guide/#overview)

[Repo](https://github.com/junit-team/junit5)

[Samples](https://github.com/junit-team/junit5-samples)

For this session, we are going to use the junit5-modular-world folder

[JShell](https://docs.oracle.com/javase/9/jshell/introduction-jshell.htm#JSHEL-GUID-630F27C8-1195-4989-9F6B-2C51D46F52C8)

1. Open an instance of Cloud9
2. Clone the JUnit Sample repo
```
git clone https://github.com/junit-team/junit5-samples.git
```
3. Experiment with the source code
Code
```
public int subs(int a, int b) {
		return a - b;
	}
```
Test
```
@Test
	void subs() {
		Assertions.assertEquals(4, calculator.subs(6, 3), "6 - 3 should equal 3");
	}
```



