// This is just a placeholder SVG-based icon
// You may want to replace it with a proper PNG/ICO file
const canvas = document.createElement('canvas');
canvas.width = 128;
canvas.height = 128;
const ctx = canvas.getContext('2d');

// Draw a gradient background
const gradient = ctx.createRadialGradient(64, 64, 0, 64, 64, 64);
gradient.addColorStop(0, '#4CAF50');
gradient.addColorStop(1, '#1E3C72');
ctx.fillStyle = gradient;
ctx.fillRect(0, 0, 128, 128);

// Draw a ball
ctx.fillStyle = 'white';
ctx.beginPath();
ctx.arc(64, 64, 40, 0, Math.PI * 2);
ctx.fill();

// Add some shine
ctx.fillStyle = 'rgba(255, 255, 255, 0.3)';
ctx.beginPath();
ctx.arc(48, 48, 15, 0, Math.PI * 2);
ctx.fill();

// Convert to data URL
const dataUrl = canvas.toDataURL('image/png');
console.log(dataUrl);
