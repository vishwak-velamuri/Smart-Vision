import React, { useRef, useEffect, useState } from 'react';
import Webcam from 'react-webcam';
import * as tf from '@tensorflow/tfjs';
import * as cocoSsd from '@tensorflow-models/coco-ssd';
import 'Smart-Vision/client/src/styles/Camera.css';

function Camera() {
  const webcamRef = useRef(null);
  const canvasRef = useRef(null);
  const [model, setModel] = useState(null);

  useEffect(() => {
    // Load COCO-SSD model
    const loadModel = async () => {
      const loadedModel = await cocoSsd.load();
      setModel(loadedModel);
    };
    loadModel();
  }, []);

  const detect = async () => {
    if (model && webcamRef.current && webcamRef.current.video.readyState === 4) {
      // Get video properties
      const video = webcamRef.current.video;
      const videoWidth = webcamRef.current.video.videoWidth;
      const videoHeight = webcamRef.current.video.videoHeight;

      // Set canvas height and width
      canvasRef.current.width = videoWidth;
      canvasRef.current.height = videoHeight;

      // Make detections
      const predictions = await model.detect(video);

      // Draw bounding boxes
      const ctx = canvasRef.current.getContext('2d');
      drawBoundingBoxes(predictions, ctx);
    }
  };

  const drawBoundingBoxes = (predictions, ctx) => {
    predictions.forEach(prediction => {
      const [x, y, width, height] = prediction.bbox;
      ctx.strokeStyle = '#00FFFF';
      ctx.lineWidth = 2;
      ctx.strokeRect(x, y, width, height);
      ctx.fillStyle = '#00FFFF';
      ctx.fillText(
        `${prediction.class} (${Math.round(prediction.score * 100)}%)`,
        x,
        y > 10 ? y - 5 : 10
      );
    });
  };

  useEffect(() => {
    const interval = setInterval(() => {
      detect();
    }, 100);
    return () => clearInterval(interval);
  }, [model]);

  return (
    <div className="camera-container">
      <Webcam
        ref={webcamRef}
        muted={true}
        style={{
          position: 'absolute',
          marginLeft: 'auto',
          marginRight: 'auto',
          left: 0,
          right: 0,
          textAlign: 'center',
          zIndex: 9,
          width: 640,
          height: 480,
        }}
      />
      <canvas
        ref={canvasRef}
        style={{
          position: 'absolute',
          marginLeft: 'auto',
          marginRight: 'auto',
          left: 0,
          right: 0,
          textAlign: 'center',
          zIndex: 10,
        }}
      />
    </div>
  );
}

export default Camera;