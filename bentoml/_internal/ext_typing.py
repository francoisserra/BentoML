from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import typing as t
    from typing import Literal

    from numpy import generic as NpGeneric
    from pandas import Series as PdSeries  # type: ignore[reportMissingTypeStubs]
    from pandas import DataFrame as PdDataFrame  # type: ignore[reportMissingTypeStubs]
    from numpy.typing import NDArray as NpNDArray
    from pyarrow.plasma import ObjectID
    from pyarrow.plasma import PlasmaClient

    DataFrameOrient = Literal["split", "records", "index", "columns", "values", "table"]
    SeriesOrient = Literal["split", "records", "index", "table"]

    from starlette.types import ASGIApp

    class AsgiMiddleware(t.Protocol):
        def __call__(self, app: ASGIApp, **options: t.Any) -> ASGIApp:
            ...

    __all__ = [
        "PdSeries",
        "PdDataFrame",
        "NpNDArray",
        "ObjectID",
        "PlasmaClient",
        "NpGeneric",
        "DataFrameOrient",
        "SeriesOrient",
        "AsgiMiddleware",
        "ASGIApp",
    ]
