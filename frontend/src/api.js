const API_BASE_URL = (process.env.REACT_APP_API_URL || "http://localhost:5000").replace(/\/$/, "");

export async function apiRequest(path, options = {}) {
  const response = await fetch(`${API_BASE_URL}${path}`, options);
  const data = await response.json().catch(() => ({}));

  if (!response.ok) {
    throw new Error(data.error || `Request failed with status ${response.status}`);
  }

  return data;
}

const speciesImages = {
  bird: "/bird.jpg",
  cat: "/cat.jpg",
  dog: "/dog.jpg",
  equine: "/equine.jpg",
  hamster: "/rodent.jpg",
  parrot: "/bird.jpg",
  rabbit: "/rodent.jpg",
  reptile: "/reptile.jpg",
};

export function getPetImage(pet) {
  if (pet?.name?.toLowerCase() === "max") {
    return "/max.jpg";
  }
  return speciesImages[pet?.species?.toLowerCase()] || "/logo512.png";
}
