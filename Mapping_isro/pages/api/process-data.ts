import { NextApiRequest, NextApiResponse } from 'next';

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === 'POST') {
    const data = req.body;
    // Process the data here
    console.log(data);
    res.status(200).json({ message: 'Data processed successfully' });
  } else {
    res.status(405).json({ message: 'Method not allowed' });
  }
}
