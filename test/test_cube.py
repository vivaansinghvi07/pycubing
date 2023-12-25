import unittest

from pycubing import Cube
from pycubing.cube import Cube3x3

SOLVED_CUBE_3X3 = "gggggggggooooooooobbbbbbbbbrrrrrrrrrwwwwwwwwwyyyyyyyyy"
EXAMPLE_SCRAMBLE_3X3 = "U2 F2 D2 B' D2 B R2 U2 F' D L R' D B2 U B2 R' B R' B2"
EXAMPLE_SCRAMBLE_6X6 = "U2 F 3Rw2 Uw R2 F 3Rw2 L B Uw F2 3Uw' Rw' D2 Rw2 3Rw2 D U 3Uw2 3Fw2 3Rw2 Dw' F2 Bw D2 F' Bw' 3Uw 3Rw' 3Uw Rw B D' R' Dw L 3Uw2 D2 3Fw' F D2 Rw' 3Rw' Dw2 Fw2 Lw2 F2 U2 D 3Rw 3Uw' B F R' 3Rw' Bw2 3Uw2 Fw' F' Dw2 Fw L' Rw 3Rw 3Uw Uw2 Fw L2 3Rw R' F L 3Fw' 3Uw' Bw2 3Uw2 U2 D2 Bw2 D2" 

class TestCube(unittest.TestCase):

    # this function is assumed to not break, as it is used to test all other cases
    def test_simple_string(self):
        cube = Cube3x3()
        self.assertEqual(cube.to_simple_string(), SOLVED_CUBE_3X3)
        example_simple_string = "bgrbyogbggoogoorywrrygrrwgrybobyywbwoorgobgwygrbgbwbwryygyrrybbwbybyrgbwwwwrwywboorbobgrrgyryborbgboowrrrgybyobgwbooowogyyywgooobwggowyrwygwwwroyrygwg"
        self.assertEqual(example_simple_string, Cube.from_simple_string(example_simple_string).to_simple_string())

    def test_scramble(self):
        for N in [2, 3, 5, 8]:
            cube, scrambled = Cube(N), Cube(N)
            scrambled.scramble()
            self.assertNotEqual(cube.to_simple_string(), scrambled.to_simple_string()) 

    def test_parse(self):  # if parsing works, the individual turning also works
        cube = Cube(6)
        cube.parse(EXAMPLE_SCRAMBLE_6X6)
        self.assertEqual(cube.to_simple_string(), 'royyrwwywowoyggybgorrowywororggrggggoyrwowwwooogbybrroyyrowwrwgbbbbbowwrbbborwgbybrrrgbgbrowwwwgobbyoggoggyybbwryybgywywwbrygyrogggbyyrgggyrwboygybyyrbbbogrgoyogwbobbyogwyrgwbybgwoooowbrrobrrwygywyrbrwowrorwrygwboryo')

    def test_get_3x3(self):
        with self.assertRaises(AssertionError):
            cube = Cube(6)
            cube.parse(EXAMPLE_SCRAMBLE_6X6)
            cube.get_3x3()
        self.assertEqual(Cube(5).get_3x3().to_simple_string(), SOLVED_CUBE_3X3)

    def test_get_rotation_to(self):
        solved_3x3 = Cube(3)
        for test_case in ["x y", "z' y", "x2"]:
            cube = Cube(3)
            cube.parse(test_case)
            cube.parse(cube.get_rotation_to(solved_3x3))
            self.assertEqual(cube.to_simple_string(), SOLVED_CUBE_3X3)

if __name__ == "__main__":
    unittest.main()
