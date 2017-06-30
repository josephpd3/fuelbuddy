import React from 'react';
import { withGoogleMap, GoogleMap, Marker } from "react-google-maps";

const FuelReportMap = withGoogleMap(props => (
    <GoogleMap
        defaultZoom={3}
        defaultCenter={{ lat: 39.8283, lng: -98.5795 }}
    >
        {props.fuelMarkers.map((marker, index) => (
            <Marker 
                {...marker}
            />
        ))}
    </GoogleMap>
));