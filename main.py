#coding=utf-8
import bruteforce_method
import dichotomy_method
import fibonachi_method
import golden_selection_method
import dichotomy_method_SECOND

#main
print('\n')
print("1 - параболическая и функции близкие к ней по кривизне")
bruteforce_method.bruteforce_method(1)
dichotomy_method.dichotomy_method(1)
golden_selection_method.golden_selection_method(1)
fibonachi_method.fibonacci_method(1)
dichotomy_method_SECOND.dichotomy_method_SECOND(1)
print('\n')
print("2 - гладкие")
bruteforce_method.bruteforce_method(2)
dichotomy_method.dichotomy_method(2)
golden_selection_method.golden_selection_method(2)
fibonachi_method.fibonacci_method(2)
dichotomy_method_SECOND.dichotomy_method_SECOND(2)
print('\n')
print("3 - пологие (медленно меняющиеся)")
bruteforce_method.bruteforce_method(3)
dichotomy_method.dichotomy_method(3)
golden_selection_method.golden_selection_method(3)
fibonachi_method.fibonacci_method(3)
dichotomy_method_SECOND.dichotomy_method_SECOND(3)
print('\n')
print("4 - негладкие")
bruteforce_method.bruteforce_method(4)
dichotomy_method.dichotomy_method(4)
golden_selection_method.golden_selection_method(4)
fibonachi_method.fibonacci_method(4)
dichotomy_method_SECOND.dichotomy_method_SECOND(4)
print('\n')
print("5 - монотонные")
bruteforce_method.bruteforce_method(5)
dichotomy_method.dichotomy_method(5)
golden_selection_method.golden_selection_method(5)
fibonachi_method.fibonacci_method(5)
dichotomy_method_SECOND.dichotomy_method_SECOND(5)
