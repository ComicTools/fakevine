# ruff: noqa: TRY003, EM101
from pathlib import Path

from loguru import logger
from sqlalchemy import Engine, create_engine, select
from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import text

from fakevine.models import cvapimodels as api
from fakevine.models import cvdbmodels as db
from fakevine.models.cvapimodels import CVResponse
from fakevine.trunks.comic_trunk import (
    ComicTrunk,
    UnsupportedResponseError,
)


class StaticDBTrunk(ComicTrunk):
    def __init__(self, database_path: Path):
        self.db_engine: Engine = create_engine(f"sqlite:///{database_path.absolute()}")
        self.session = Session(self.db_engine)

        try:
            with self.db_engine.connect() as conn:
                _ = conn.execute(text("SELECT 'hello engine'"))
        except DatabaseError:
            logger.exception("Input database is not a valid SQL database")
            raise

        # TODO@falo2k: Validate database schema

    def character(self, item_id: int, params: api.CommonParams) -> api.SingleResponse[api.DetailCharacter]:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def characters(self, params: api.CommonParams) -> api.MultiResponse[api.BaseCharacter]:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def concept(self, item_id: int, params: api.CommonParams) -> api.SingleResponse[api.DetailConcept]:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def concepts(self, params: api.CommonParams) -> api.MultiResponse[api.BaseConcept]:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def issue(self, item_id: int, params: api.CommonParams) -> api.SingleResponse[api.DetailIssue]:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def issues(self, params: api.CommonParams) -> api.MultiResponse[api.BaseIssue]:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def location(self, item_id: int, params: api.CommonParams) -> api.SingleResponse[api.DetailLocation]:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def locations(self, params: api.CommonParams) -> api.MultiResponse[api.BaseLocation]:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def object(self, item_id: int, params: api.CommonParams) -> api.SingleResponse[api.DetailObject]:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def objects(self, params: api.CommonParams) -> api.MultiResponse[api.BaseObject]:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def origin(self, item_id: int, params: api.CommonParams) -> api.SingleResponse[api.DetailOrigin]:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def origins(self, params: api.CommonParams) -> api.MultiResponse[api.BaseOrigin]:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def person(self, item_id: int, params: api.CommonParams) -> api.SingleResponse[api.DetailPerson]:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def people(self, params: api.CommonParams) -> api.MultiResponse[api.BasePerson]:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def power(self, item_id: int, params: api.CommonParams) -> api.SingleResponse[api.DetailPower]:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def powers(self, params: api.CommonParams) -> api.MultiResponse[api.BasePower]:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def publisher(self, item_id: int, params: api.CommonParams) -> api.SingleResponse[api.DetailPublisher]:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def publishers(self, params: api.CommonParams) -> api.MultiResponse[api.BasePublisher]:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def search(self, params: api.SearchParams) -> api.SearchResponse:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def story_arc(self, item_id: int, params: api.CommonParams) -> api.SingleResponse[api.DetailStoryArc]:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def story_arcs(self, params: api.CommonParams) -> api.MultiResponse[api.BaseStoryArc]:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def team(self, item_id: int, params: api.CommonParams) -> api.SingleResponse[api.DetailTeam]:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def teams(self, params: api.CommonParams) -> api.MultiResponse[api.BaseTeam]:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def volume(self, item_id: int, params: api.CommonParams) -> api.SingleResponse[api.DetailVolume]:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def volumes(self, params: api.FilterParams) -> api.MultiResponse[api.BaseVolume]:
        raise UnsupportedResponseError("Route not implemented by trunk")


    ## The trunk only supports comic data
    def episode(self, item_id: int, params: api.CommonParams) -> api.CVResponse:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def episodes(self, params: api.CommonParams) -> api.CVResponse:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def movie(self, item_id: int, params: api.CommonParams) -> api.CVResponse:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def movies(self, params: api.CommonParams) -> api.CVResponse:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def series(self, item_id: int, params: api.CommonParams) -> api.CVResponse:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def series_list(self, params: api.CommonParams) -> api.CVResponse:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def video(self, item_id: int, params: api.CommonParams) -> api.CVResponse:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def videos(self, params: api.CommonParams) -> api.CVResponse:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def video_type(self, item_id: int, params: api.CommonParams) -> api.CVResponse:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def video_types(self, params: api.CommonParams) -> api.CVResponse:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def video_category(self, item_id: int, params: api.CommonParams) -> api.CVResponse:
        raise UnsupportedResponseError("Route not implemented by trunk")

    def video_categories(self, params: api.CommonParams) -> api.CVResponse:
        raise UnsupportedResponseError("Route not implemented by trunk")