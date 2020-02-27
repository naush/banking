## Kata Workshop

### Problem

Create a banking application with the following features:

* Deposit into Account
* Withdraw from an Account
* Print a Bank Statement

### Examples

**Given** a client makes a deposit of 1000 on 10-01-2012

**And** a deposit of 2000 on 13-01-2012

**And** a withdrawal of 500 on 14-01-2012

**When** she prints her bank statement

**Then** she would see

| Date       | Credit   | Debit    | Balance |
| ---        | ---      | ---      | ---     |
| 14/01/2012 |          | 500      | 2500    |
| 13/01/2012 | 2000     |          | 3000    |
| 10/01/2012 | 1000     |          | 1000    |

### Constraints

1. One level of indentation per method
2. Don’t use the ELSE keyword
3. Wrap all primitives and Strings
4. First class collections
5. One dot per line
6. Don’t abbreviate
7. Keep all entities small (50 lines)
8. No classes with more than two instance variables
9. No getters/setters/properties

### Learning Outcomes

* [The Four-Phase Test](https://thoughtbot.com/blog/four-phase-test)
* [Three Rules of TDD](https://blog.gowtham-sai.com/three-laws-of-tdd-a84dd5204eae)
* Test Doubles
* Inside-Out and Outside-In Development

### Resources

* [Bank on Katalyst](https://katalyst.codurance.com/bank)
* [Object Calisthenics](https://www.cs.helsinki.fi/u/luontola/tdd-2009/ext/ObjectCalisthenics.pdf)
* [unittest.mock documentation](https://docs.python.org/3/library/unittest.mock-examples.html)
