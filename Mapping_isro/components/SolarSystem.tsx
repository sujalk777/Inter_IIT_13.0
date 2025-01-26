// components/SolarSystem.tsx
import { useEffect, useRef } from 'react';
import * as THREE from 'three';

const SolarSystem = () => {
  const mountRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const mount = mountRef.current;
    if (!mount) return;

    // Scene
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x000000); // Black background

    // Camera
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.z = 5;

    // Renderer
    const renderer = new THREE.WebGLRenderer({ alpha: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    mount.appendChild(renderer.domElement);

    // Texture Loader
    const textureLoader = new THREE.TextureLoader();

    // Solar System
    const sunTexture = textureLoader.load('/img/sun.jpg');
    const sunGeometry = new THREE.SphereGeometry(0.5, 32, 32);
    const sunMaterial = new THREE.MeshBasicMaterial({ map: sunTexture });
    const sun = new THREE.Mesh(sunGeometry, sunMaterial);
    scene.add(sun);

    const planetTextures = [
      '/img/mercury.jpg',
      '/img/venus.jpg',
      '/img/earth.jpg',
      '/img/mars.jpg',
      '/img/jupiter.jpg',
      '/img/saturn.jpg',
      '/img/uranus.jpg',
      '/img/neptune.jpg',
    ];

    const planets: THREE.Mesh[] = [];
    for (let i = 0; i < 8; i++) {
      const planetTexture = textureLoader.load(planetTextures[i]);
      const planetGeometry = new THREE.SphereGeometry(0.2, 32, 32);
      const planetMaterial = new THREE.MeshBasicMaterial({ map: planetTexture });
      const planet = new THREE.Mesh(planetGeometry, planetMaterial);
      planet.position.x = (i + 1) * 1.5;
      scene.add(planet);
      planets.push(planet);
    }

    // Stars
    const starGeometry = new THREE.BufferGeometry();
    const starMaterial = new THREE.PointsMaterial({ color: 0xffffff });

    const starVertices = [];
    for (let i = 0; i < 1000; i++) {
      const x = (Math.random() - 0.5) * 2000;
      const y = (Math.random() - 0.5) * 2000;
      const z = (Math.random() - 0.5) * 2000;
      starVertices.push(x, y, z);
    }
    starGeometry.setAttribute('position', new THREE.Float32BufferAttribute(starVertices, 3));

    const stars = new THREE.Points(starGeometry, starMaterial);
    scene.add(stars);

    // Animation
    const animate = () => {
      requestAnimationFrame(animate);

      sun.rotation.y += 0.002; // Reduced speed
      planets.forEach((planet, index) => {
        planet.rotation.y += 0.002; // Reduced speed
        planet.position.x = Math.cos(Date.now() * 0.0005 + index) * (index + 1) * 1.5; // Reduced speed
        planet.position.z = Math.sin(Date.now() * 0.0005 + index) * (index + 1) * 1.5; // Reduced speed
      });

      renderer.render(scene, camera);
    };
    animate();

    // Cleanup
    return () => {
      mount.removeChild(renderer.domElement);
    };
  }, []);

  return <div ref={mountRef} style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', zIndex: -1 }} />;
};

export default SolarSystem;