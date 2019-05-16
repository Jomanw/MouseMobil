import React, { Component } from 'react';
import JoyWrapper from './JoyWrapper.js';
const request = require("request");


class ControlButtons extends Component {
    constructor() {
        super();
        this.state = {
            testMode: true,
        }
        this.render=this.render.bind(this);
        this.runCar=this.runCar.bind(this);
        this.testMode=this.testMode.bind(this);
    }

    runCar() {
        this.setState({
            testMode: false,
        });
        request.post('http://mousemobil.ddns.net/runautonomous', {});
    }

    stopCar() {
        request.post('http://mousemobil.ddns.net/stopcar', {});
        request.post('http://mousemobil.ddns.net/opendoor', {});
    }

    setCarPosition() {
        this.props.setCarPosition();
    }

    testMode() {
        this.setState({
            testMode: true,
        });
        request.post('http://mousemobil.ddns.net/runtest', {});
    }

    render() {
        const { classes } = this.props;
        var controlDashboard;
        if (this.state.testMode) {
            controlDashboard = <JoyWrapper />
        } else {
            controlDashboard = <div />
        };
        return (
            <div>
                <form>
                    <input type="button" name="run_mousemobil" value="Start MouseMobil" onClick={this.runCar} />
                    <input type="button" name="stop_car" value="Stop Car and Open Door" onClick={this.stopCar} />
                    <input type="button" name="manual_control" value="Run Car in Test Mode" onClick={this.testMode} />
                </form>
                {controlDashboard}
            </div>
        )
    }
}

export default ControlButtons;
