import unittest
from unittest.mock import patch, call

from event_scheduler import Event, schedule_events, print_schedule


class TestEventScheduler(unittest.TestCase):
    @patch("builtins.print")
    def test_schedule_events(self, mock_print):
        events = [
            # Events should be sorted
            Event("C++ Workshop", 16),
            Event("Python Workshop", 14),
            # Multiple events at the same time
            Event("Data Science Meetup", 18),
            Event("Web Dev Seminar", 18),
            # Edge case 1: Hour should not be less than 0
            Event("Wrong time event 1", -2),
            # Edge case 2: Hour should not be greater than 24
            Event("Wrong time event 2", 30),
        ]

        schedule = schedule_events(events)

        self.assertEqual(
            schedule,
            {
                14: ["Python Workshop"],
                16: ["C++ Workshop"],
                18: ["Data Science Meetup", "Web Dev Seminar"],
            },
        )
        mock_print.assert_has_calls(
            [
                call("Invalid time for event Wrong time event 1"),
                call("Invalid time for event Wrong time event 2"),
            ]
        )

    @patch("builtins.print")
    def test_schedule_events_with_empty_list(self, mock_print):
        events = []

        schedule = schedule_events(events)

        self.assertEqual(schedule, {})
        mock_print.assert_has_calls([])

    @patch("builtins.print")
    def test_print_schedule(self, mock_print):
        schedule = {
            14: ["Python Workshop"],
            16: ["C++ Workshop"],
            18: ["Data Science Meetup", "Web Dev Seminar"],
        }

        print_schedule(schedule)

        mock_print.assert_has_calls(
            [
                call("14:00 - Python Workshop"),
                call("16:00 - C++ Workshop"),
                call("18:00 - Data Science Meetup, Web Dev Seminar"),
            ]
        )

    @patch("builtins.print")
    def test_print_schedul_with_empty_events(self, mock_print):
        schedule = {}

        print_schedule(schedule)

        mock_print.assert_has_calls([])


if __name__ == "__main__":
    unittest.main()
