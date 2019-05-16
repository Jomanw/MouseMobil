import React, { Component } from 'react';
import JoyStick from "react-joystick";
const request = require("request");

const joyStickSize = 300;

const joyOptions = {
    mode: 'dynamic',
    size: joyStickSize,
    catchDistance: 50,
    fadeTime: 500,
    color: 'orange',
    threshold: .9,
    position: {
        top: '50%',
        left: '50%'
    }
}

const containerStyle = {
    position: 'relative',
    height: '100%',
    width: '100%',
    background: 'blue'
}


class JoyWrapper extends Component {
    constructor() {
        super();
        this.managerListener = this.managerListener.bind(this);
        this.stopCar = this.stopCar.bind(this);
        this.setCarVelocity = this.setCarVelocity.bind(this);
    }

    stopCar() {
        request.post('http://mousemobil.ddns.net/stopcar', {});
    }

    setCarVelocity(x, y) {
        request.post('http://mousemobil.ddns.net/setspeed', {x:x, y:y});
    }

    managerListener(manager) {
        manager.on('move', (e, stick) => {
            var radian = stick.angle.radian;
            var magnitude = 2 * stick.distance / joyStickSize;
            var dx = Math.cos(radian) * magnitude;
            var dy = Math.sin(radian) * magnitude;
            console.log(dx);
            console.log(dy);
            this.setCarVelocity(dx, dy);

        })

        manager.on('end', () => {
            this.stopCar();
            console.log("Stopped the car.");
        })
    }

    render() {
        const { classes } = this.props;
        return (
            <div>
                <JoyStick options={joyOptions} containerStyle={containerStyle} managerListener={this.managerListener} />
            </div>
        )
    }
}

export default JoyWrapper;
