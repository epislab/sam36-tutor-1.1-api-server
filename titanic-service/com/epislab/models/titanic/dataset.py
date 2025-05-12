from dataclasses import dataclass


@dataclass
class Dataset:
    context: str
    fname: str
    train: object
    test: object
    id: str
    label: str

    @property
    def context(self) -> str: return self._context

    @property
    def fname(self) -> str: return self._fname

    @property
    def train(self) -> object: return self._train

    @property
    def test(self) -> object: return self._test

    @property
    def id(self) -> str: return self._id

    @property
    def label(self) -> str: return self._label

    @context.setter
    def context(self, context): self._context = context

    @fname.setter
    def fname(self, fname): self._fname = fname

    @train.setter
    def train(self, train): self._train = train

    @test.setter
    def test(self, test): self._test = test

    @id.setter
    def id(self, id): self._id = id

    @label.setter
    def label(self, label): self._label = label