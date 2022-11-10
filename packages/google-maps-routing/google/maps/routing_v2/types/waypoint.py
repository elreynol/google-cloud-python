# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import proto  # type: ignore

from google.maps.routing_v2.types import location as gmr_location

__protobuf__ = proto.module(
    package="google.maps.routing.v2",
    manifest={
        "Waypoint",
    },
)


class Waypoint(proto.Message):
    r"""Encapsulates a waypoint. Waypoints mark both the beginning
    and end of a route, and include intermediate stops along the
    route.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        location (google.maps.routing_v2.types.Location):
            A point specified using geographic
            coordinates, including an optional heading.

            This field is a member of `oneof`_ ``location_type``.
        place_id (str):
            The POI Place ID associated with the
            waypoint.

            This field is a member of `oneof`_ ``location_type``.
        via (bool):
            Marks this waypoint as a milestone rather a stopping point.
            For each non-via waypoint in the request, the response
            appends an entry to the ``legs`` array to provide the
            details for stopovers on that leg of the trip. Set this
            value to true when you want the route to pass through this
            waypoint without stopping over. Via waypoints don't cause an
            entry to be added to the ``legs`` array, but they do route
            the journey through the waypoint. You can only set this
            value on waypoints that are intermediates. The request fails
            if you set this field on terminal waypoints. If
            ``ComputeRoutesRequest.optimize_waypoint_order`` is set to
            true then this field cannot be set to true; otherwise, the
            request fails.
        vehicle_stopover (bool):
            Indicates that the waypoint is meant for vehicles to stop
            at, where the intention is to either pickup or drop-off.
            When you set this value, the calculated route won't include
            non-\ ``via`` waypoints on roads that are unsuitable for
            pickup and drop-off. This option works only for ``DRIVE``
            and ``TWO_WHEELER`` travel modes, and when the
            ``location_type`` is ``location``.
        side_of_road (bool):
            Indicates that the location of this waypoint is meant to
            have a preference for the vehicle to stop at a particular
            side of road. When you set this value, the route will pass
            through the location so that the vehicle can stop at the
            side of road that the location is biased towards from the
            center of the road. This option works only for 'DRIVE' and
            'TWO_WHEELER' travel modes.
    """

    location = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="location_type",
        message=gmr_location.Location,
    )
    place_id = proto.Field(
        proto.STRING,
        number=2,
        oneof="location_type",
    )
    via = proto.Field(
        proto.BOOL,
        number=3,
    )
    vehicle_stopover = proto.Field(
        proto.BOOL,
        number=4,
    )
    side_of_road = proto.Field(
        proto.BOOL,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
