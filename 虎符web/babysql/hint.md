```sql
CREATE TABLE `auth` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `password` varchar(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_username_uindex` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

```js
import { Injectable } from '@nestjs/common';
import { ConnectionProvider } from '../database/connection.provider';

export class User {
  id: number;
  username: string;
}

function safe(str: string): string {
  const r = str
    .replace(/[\s,()#;*\-]/g, '')
    .replace(/^.*(?=union|binary).*$/gi, '')
    .toString();
  return r;
}

@Injectable()
export class AuthService {
  constructor(private connectionProvider: ConnectionProvider) {}

  async validateUser(username: string, password: string): Promise<User> | null {
    const sql = `SELECT * FROM auth WHERE username='${safe(username)}' LIMIT 1`;
    const [rows] = await this.connectionProvider.use((c) => c.query(sql));
    const user = rows[0];
    if (user && user.password === password) {
      // eslint-disable-next-line @typescript-eslint/no-unused-vars
      const { password, ...result } = user;
      return result;
    }
    return null;
  }
}
```