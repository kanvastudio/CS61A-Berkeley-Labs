test = {
  'name': 'Question 4',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> num_factors(1)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> num_factors(2)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> num_factors(3)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> num_factors(9)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> num_factors(28)
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> num_factors(64)
          7
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> num_factors(72)
          12
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> num_factors(97)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> num_factors(99)
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_points(1)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_points(21)
          23
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_points(25)
          29
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_points(62)
          67
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_points(64)
          64
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_points(67)
          67
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_points(75)
          75
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_points(86)
          89
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_points(100)
          100
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> simple_update(2, 5, 7, make_test_dice(2, 4))
          11
          >>> sus_update(2, 5, 7, make_test_dice(2, 4)) # is 11 a sus number?
          11
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> simple_update(0, 15, 37) # what happens when you roll 0 dice?
          383b6800a83090c27da97b04ffebb176
          # locked
          >>> sus_update(0, 15, 37) # is 21 a sus number?
          f8205a9c61f815c0fdd6e3d5c81074b7
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> simple_update(2, 2, 3, make_test_dice(4))
          8a27d52d885dfcd62a4a92cbfe64d30a
          # locked
          >>> sus_update(2, 2, 3, make_test_dice(4)) # is 10 a sus number?
          62d21c0af6a781863aa95a5ba2138e77
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_update(3, 11, 12, make_test_dice(4, 5, 6))
          29
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_update(2, 29, 17, make_test_dice(1, 3))
          30
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_update(0, 41, 42)
          50
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_update(0, 40, 22)
          47
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_update(2, 56, 56, make_test_dice(4))
          64
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> import types
          >>> def imports():
          ...     for name, val in globals().items():
          ...         if isinstance(val, types.ModuleType):
          ...             yield val.__name__
          >>> list(imports()) # do NOT import any new modules!
          ['tests.construct_check', 'types']
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      >>> import tests.construct_check as test
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
