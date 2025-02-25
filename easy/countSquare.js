function countSquares(cuts) {
  if (cuts === 0) return 1;
  const total = (cuts + 1) ** 3;
  const internal = (cuts - 1) ** 3;
  return total - internal;
}

// (cuts + 1) ^ 3 => 27, 125
// (cuts - 1) ^ 3 => 1
