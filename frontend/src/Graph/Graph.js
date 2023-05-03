import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

function Graph( { samples } ) {

    //let data = samples;
    let data = [
        {
          "moisture": 0.33,
          "temperature": 23.4,
          "timestamp": "2023-04-25 17:42:08"
      },
      {
          "moisture": 0.33,
          "temperature": 23.4,
          "timestamp": "2023-04-24 17:45:28"
      }
    ];

    data = samples;

    return (
        <ResponsiveContainer width="100%" height="100%">
          <LineChart
            width={'100%'} height={300}
            data={samples}
            redraw={true}
            margin={{
              top: 5,
              right: 30,
              left: 20,
              bottom: 5,
            }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="timestamp" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="temperature" stroke="#8884d8" activeDot={{ r: 8 }} />
            <Line type="monotone" dataKey="moisture" stroke="#82ca9d" />
          </LineChart>
        </ResponsiveContainer>
      );
}

export default Graph;
