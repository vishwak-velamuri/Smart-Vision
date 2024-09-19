import React, { useRef, useEffect, useState } from 'react';
import Webcam from 'react-webcam';
import * as tf from '@tensorflow/tfjs';
import * as cocoSsd from '@tensorflow-models/coco-ssd'; // Ensure this module is installed
import './styles/Camera.css'; // Adjust path based on actual file location

function Camera() {
  const webcamRef = useRef(null);
  const canvasRef = useRef(null);
  const [model, setModel] = useState(null);

  useEffect(() => {
    const loadModel = async () => {
      try {
        const loadedModel = await cocoSsd.load();
        setModel(loadedModel);
      } catch (error) {
        console.error("Error loading COCO-SSD model:", error);
      }
    };
    loadModel();
  }, []);

  const detect = async () => {
    if (model && webcamRef.current && webcamRef.current.video.readyState === 4) {
      const video = webcamRef.current.video;
      const videoWidth = video.videoWidth;
      const videoHeight = video.videoHeight;

      canvasRef.current.width = videoWidth;
      canvasRef.current.height = videoHeight;

      try {
        const predictions = await model.detect(video);
        const ctx = canvasRef.current.getContext('2d');
        if (ctx) {
          drawBoundingBoxes(predictions, ctx);
        }
      } catch (error) {
        console.error("Error during detection:", error);
      }
    }
  };

  const drawBoundingBoxes = (predictions, ctx) => {
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
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
    }, 500); // Adjust interval as needed
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
