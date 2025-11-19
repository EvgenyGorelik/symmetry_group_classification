import numpy as np
from argparse import ArgumentParser
import spglib as spg

class ResReader:
    def __init__(self, path):
        with open(path, 'r') as f:
            content = f.readlines()
        self.cell_values = np.array([
            float(content[1][13:22]),
            float(content[1][22:31]),
            float(content[1][31:40]),
            float(content[1][40:49]),
            float(content[1][49:58]),
            float(content[1][58:67]),
        ])
        self.types = []
        self.atoms = []
        for i in range(4, len(content) - 1):
            self.types.append(content[i][4:7])
            self.atoms.append(
                [
                    float(content[i][7:18]),
                    float(content[i][18:29]),
                    float(content[i][29:40]),
                ]
            )
        self.atoms = np.array(self.atoms)


def get_spglib_group(spacegroup_number):
    sym = spg.get_symmetry_from_database(spacegroup_number)
    rotations = sym['rotations']
    translations = sym['translations']
    group = []
    for r, t in zip(rotations, translations):
        mat = np.eye(4)
        mat[:3, :3] = r
        mat[:3, 3] = t
        group.append(mat)
    return group


def check_symmetry(group, atoms, types=None, eps=1e-5):
    assert atoms.ndim == 2 and atoms.shape[1] == 3
    atoms_h = np.hstack([atoms, np.ones((atoms.shape[0], 1))])
    for t in group:
        for i, c in enumerate(atoms_h):
            r = c @ t
            r = r + np.array(r < 0)
            r = r - np.array(r > 1)
            dists = np.linalg.norm(atoms - r[:3], axis=1)
            if not np.any(dists < eps):
                return False
            if types is not None:
                idx = np.argmin(dists)
                if types[idx] != types[i]:
                    return False
    return True


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--file", type=str, default=None, help="Atomic file to read")
    parser.add_argument("--eps", type=float, default=1e-5, help="Tolerance for symmetry check")
    args = parser.parse_args()

    if args.file is None:
        atoms = np.array([[0, 0, 0], [1 / 3, 2 / 3, 0], [1 / 2, 1 / 3, 0]])
        types = [0, 0, 1]

        print("Using default structure")
        print("Atoms:")
        print(atoms)
        print("Types:")
        print(types)


        for sg in range(1, 231):
            group = get_spglib_group(sg)
            if check_symmetry(group, atoms, types, eps=args.eps):
                print(f"Spacegroup {sg} is a symmetry group of the structure")
    else:
        res = ResReader(args.file)

        print("Cell Values:")
        print(res.cell_values)
        print("Atoms:")
        print(res.atoms)
        print("Types:")
        print(res.types)

        for sg in range(1, 231):
            group = get_spglib_group(sg)
            if check_symmetry(group, res.atoms, res.types, eps=args.eps):
                print(f"Spacegroup {sg} is a symmetry group of the structure")

    # TODO: implement origin shift (origin_shift = np.array([0.1, 0.2, 0.3]))