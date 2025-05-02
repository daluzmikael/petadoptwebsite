// src/pages/Events.jsx

import EventCard from '../components/eventcard';

export default function Events() {
  const events = [
    {
      title: "Adopt-a-thon Weekend",
      date: "May 4–5, 2025",
      location: "Community Center Green",
    },
    {
      title: "Puppy Yoga",
      date: "May 10, 2025",
      location: "Downtown Dog Park Pavilion",
    },
    {
      title: "Summer Cat Café Meetup",
      date: "May 15, 2025",
      location: "Pet Haven Indoor Cat Lounge",
    },
  ];

  return (
    <div className="p-6">
      <h2 className="text-3xl font-bold mb-6 text-center">Upcoming Events</h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {events.map((event, index) => (
          <EventCard
            key={index}
            title={event.title}
            date={event.date}
            location={event.location}
          />
        ))}
      </div>
    </div>
  );
}
