import pytest
from ut_frameworks import AcceptanceThreshold, MergeRequest, MergeRequestStatus


@pytest.mark.parametrize(
    "context,expected_status",
    (
        (
            {"downvotes": set(), "upvotes": set()},
            MergeRequestStatus.PENDING,
        ),
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
    ),
)
def test_acceptance_threshold_status_resolution(context, expected_status):
    assert AcceptanceThreshold(context).status() == expected_status


# Stacking will create a cartesian product
# @pytest.mark.parametrize(
#     "context",
#     (
#         {"downvotes": set(), "upvotes": set()},
#         {"downvotes": set(), "upvotes": {"dev1"}},
#         {"downvotes": {"dev1"}, "upvotes": set()},
#         {"downvotes": {"dev1"}, "upvotes": {"dev1"}},
#     ),
# )
# @pytest.mark.parametrize(
#     "expected_status",
#     (MergeRequestStatus.PENDING, MergeRequestStatus.REJECTED, MergeRequestStatus.APPROVED),
# )
# def test_acceptance_threshold_status_resolution_cartesian(context, expected_status):
#     assert AcceptanceThreshold(context).status() == expected_status


@pytest.fixture
def rejected_mr():
    merge_request = MergeRequest()

    merge_request.downvote("dev1")
    merge_request.upvote("dev2")
    merge_request.upvote("dev3")
    merge_request.downvote("dev4")

    return merge_request


def test_simple_rejected(rejected_mr):
    assert rejected_mr.status == MergeRequestStatus.REJECTED


def test_rejected_with_approvals(rejected_mr):
    rejected_mr.upvote("dev2")
    rejected_mr.upvote("dev3")
    assert rejected_mr.status == MergeRequestStatus.REJECTED


def test_rejected_to_pending(rejected_mr):
    rejected_mr.upvote("dev1")
    assert rejected_mr.status == MergeRequestStatus.PENDING


def test_rejected_to_approved(rejected_mr):
    rejected_mr.upvote("dev1")
    rejected_mr.upvote("dev2")
    assert rejected_mr.status == MergeRequestStatus.APPROVED
