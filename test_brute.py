import pytest
from unittest.mock import Mock
from brute import Brute

todo = pytest.mark.skip(reason='todo: pending spec')

def describe_Brute():

    @pytest.fixture
    def cracker():
        return Brute("TDD")

    def describe_bruteOnce():
        # write your test cases here
        def normal_brute_activity():
            b = Brute("Do or do not. There is no try.")
            guess = b.randomGuess()
            assert b.bruteOnce(guess) == False


        def all_caps():
            b = Brute("DO OR DO NOT. THERE IS NO TRY")
            guess = b.randomGuess()
            assert b.bruteOnce(guess) == False

        def all_lower():
            b = Brute("do or do not. there is no try")
            guess = b.randomGuess()
            assert b.bruteOnce(guess) == False

        def numbers_question_mark():
            b = Brute("d0 or d0 not. there is n0 try")
            guess = b.randomGuess()
            assert b.bruteOnce(guess) == False

        def how_do_we_feel_about_syntax():
            b = Brute("do or do not. there is no 'try'")
            guess = b.randomGuess()
            assert b.bruteOnce(guess) == False

        def long_message():
            b = Brute("this is a really long message that I am writing right now and someone just stood up to check off and i am freaking out but that is okay because i have time and this is just my brain")
            guess = b.randomGuess()
            assert b.bruteOnce(guess) == False

        def short_message():
            b = Brute("short")
            guess = b.randomGuess()
            assert b.bruteOnce(guess) == False

        def no_message():
            b = Brute("     ")
            guess = b.randomGuess()
            assert b.bruteOnce(guess) == False

        def what_does_empty_quotations_do():
            b = Brute("")
            guess = b.randomGuess()
            assert b.bruteOnce(guess) == False



    def describe_bruteMany():
        # write your test cases here
        def mock_many_first_try():
            external_monitor_mock = Mock()
            b = Brute("cat", external_monitor=external_monitor_mock)
            b.bruteMany(10)
            external_monitor_mock.notify_bruteMany.assert_called_once_with(10)
        
        def mock_many_better_try():
            external_monitor_mock = Mock()
            b = Brute("Do or do not. There is no try.", external_monitor=external_monitor_mock)
            b.bruteMany(1000)
            external_monitor_mock.notify_bruteMany.assert_called_once_with(1000)
        
        def mock_many_with_caps():
            external_monitor_mock = Mock()
            b = Brute("DO OR DO NOT THERE IS NO TRY", external_monitor=external_monitor_mock)
            b.bruteMany(1000)
            external_monitor_mock.notify_bruteMany.assert_called_once_with(1000)
        
        def mock_with_lower():
            external_monitor_mock = Mock()
            b = Brute("do or do not. there is no try.", external_monitor=external_monitor_mock)
            b.bruteMany(1000)
            external_monitor_mock.notify_bruteMany.assert_called_once_with(1000)
        
        def mock_with_numbers():
            external_monitor_mock = Mock()
            b = Brute("D0 or d0 n0t. There is n0 try.", external_monitor=external_monitor_mock)
            b.bruteMany(1000)
            external_monitor_mock.notify_bruteMany.assert_called_once_with(1000)
        
        def mock_with_syntax():
            external_monitor_mock = Mock()
            b = Brute("Do or do not. There is no 'try'.", external_monitor=external_monitor_mock)
            b.bruteMany(1000)
            external_monitor_mock.notify_bruteMany.assert_called_once_with(1000)
        
        def mock_with_long():
            external_monitor_mock = Mock()
            b = Brute("this is a really long message that I am writing right now and someone just stood up to check off and i am freaking out but that is okay because i have time and this is just my brain", external_monitor=external_monitor_mock)
            b.bruteMany(1000)
            external_monitor_mock.notify_bruteMany.assert_called_once_with(1000)
        
        def mock_with_short():
            external_monitor_mock = Mock()
            b = Brute("short", external_monitor=external_monitor_mock)
            b.bruteMany(1000)
            external_monitor_mock.notify_bruteMany.assert_called_once_with(1000)
        
        def mock_no_message():
            external_monitor_mock = Mock()
            b = Brute("     ", external_monitor=external_monitor_mock)
            b.bruteMany(1000)
            external_monitor_mock.notify_bruteMany.assert_called_once_with(1000)
                  
        def mock_empty_quote():
            external_monitor_mock = Mock()
            b = Brute("", external_monitor=external_monitor_mock)
            b.bruteMany(1000)
            external_monitor_mock.notify_bruteMany.assert_called_once_with(1000)
        