from unittest import TestCase, main

from mrstatus import MergeRequestException
from mrstatus import MergeRequestExtendedStatus as MergeRequestStatus
from ut_frameworks import AcceptanceThreshold
from ut_frameworks import MergeRequest as MergeRequest


class BaseCase:
    def setUp(self):
        self.merge_request = self.mr_cls()

    def test_simple_rejected(self):
        self.merge_request.downvote("maintainer")
        self.assertEqual(self.merge_request.status, MergeRequestStatus.REJECTED)

    def test_just_created_is_pending(self):
        self.assertEqual(self.mr_cls().status, MergeRequestStatus.PENDING)

    def test_pending_awaiting_review(self):
        self.merge_request.upvote("core-dev")
        self.assertEqual(self.merge_request.status, MergeRequestStatus.PENDING)

    def test_approved(self):
        self.merge_request.upvote("dev1")
        self.merge_request.upvote("dev2")

        self.assertEqual(self.merge_request.status, MergeRequestStatus.APPROVED)


class ExtendedCases:
    """For the MRs that use the extended status."""

    def test_cannot_upvote_on_closed_merge_request(self):
        self.merge_request.close()
        self.assertRaises(MergeRequestException, self.merge_request.upvote, "dev1")

    def test_cannot_downvote_on_closed_merge_request(self):
        self.merge_request.close()
        self.assertRaisesRegex(
            MergeRequestException,
            "can't vote on a closed merge request",
            self.merge_request.downvote,
            "dev1",
        )


class TestAcceptanceThreshold(TestCase):
    def setUp(self):
        self.fixture_data = (
            ({"downvotes": set(), "upvotes": set()}, MergeRequestStatus.PENDING),
            (
                {"downvotes": set(), "upvotes": {"dev1"}},
                MergeRequestStatus.PENDING,
            ),
            (
                {"downvotes": "dev1", "upvotes": set()},
                MergeRequestStatus.REJECTED,
            ),
            (
                {"downvotes": set(), "upvotes": {"dev1", "dev2"}},
                MergeRequestStatus.APPROVED,
            ),
        )

    def test_status_resolution(self):
        for context, expected in self.fixture_data:
            with self.subTest(context=context):
                status = AcceptanceThreshold(context).status()
                self.assertEqual(status, expected)


class TestsUTFrameworks1(BaseCase, ExtendedCases, TestCase):
    mr_cls = MergeRequest


class TestMergeRequestStatus(TestCase):
    def setUp(self):
        self.merge_request = MergeRequest()

    def assert_rejected(self):
        self.assertEqual(self.merge_request.status, MergeRequestStatus.REJECTED)

    def assert_pending(self):
        self.assertEqual(self.merge_request.status, MergeRequestStatus.PENDING)

    def assert_approved(self):
        self.assertEqual(self.merge_request.status, MergeRequestStatus.APPROVED)

    def test_simple_rejected(self):
        self.merge_request.downvote("maintainer")
        self.assert_rejected()

    def test_just_created_is_pending(self):
        self.assert_pending()


if __name__ == "__main__":
    main()
